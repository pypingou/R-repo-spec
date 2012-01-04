%global packname  pastecs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.11
Release:          1%{?dist}
Summary:          Package for Analysis of Space-Time Ecological Series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-stats 

BuildRequires:    R-devel tex(latex) R-boot R-stats 

%description
Regulation, decomposition and analysis of space-time series. The pastecs
library is a PNEC-Art4 and IFREMER (Benoit Beliaeff
<Benoit.Beliaeff@ifremer.fr>) initiative to bring PASSTEC 2000
(http://www.obs-vlfr.fr/~enseigne/anado/passtec/passtec.htm)
functionnalities to R.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/pastecs/DESCRIPTION
%doc %{rlibdir}/pastecs/doc
%doc %{rlibdir}/pastecs/html
%{rlibdir}/pastecs/INDEX
%{rlibdir}/pastecs/NAMESPACE
%{rlibdir}/pastecs/help
%{rlibdir}/pastecs/data
%{rlibdir}/pastecs/R
%{rlibdir}/pastecs/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.11-1
- initial package for Fedora