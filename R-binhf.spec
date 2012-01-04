%global packname  binhf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Haar-Fisz functions for binomial data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-wavethresh R-adlift 

BuildRequires:    R-devel tex(latex) R-wavethresh R-adlift 

%description
Binomial Haar-Fisz transforms for Gaussianization

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
%doc %{rlibdir}/binhf/html
%doc %{rlibdir}/binhf/DESCRIPTION
%{rlibdir}/binhf/R
%{rlibdir}/binhf/INDEX
%{rlibdir}/binhf/Meta
%{rlibdir}/binhf/help
%{rlibdir}/binhf/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora