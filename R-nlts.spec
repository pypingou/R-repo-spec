%global packname  nlts
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          (non)linear time series analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-locfit R-acepack R-akima 

BuildRequires:    R-devel tex(latex) R-locfit R-acepack R-akima 

%description
R functions for (non)linear time series analysis. A core topic is order
estimation through cross-validation.

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
%doc %{rlibdir}/nlts/html
%doc %{rlibdir}/nlts/DESCRIPTION
%{rlibdir}/nlts/NAMESPACE
%{rlibdir}/nlts/INDEX
%{rlibdir}/nlts/R
%{rlibdir}/nlts/help
%{rlibdir}/nlts/data
%{rlibdir}/nlts/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.8-1
- initial package for Fedora