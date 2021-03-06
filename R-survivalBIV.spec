%global packname  survivalBIV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Estimation of the bivariate distribution function

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-prodlim R-stats 

BuildRequires:    R-devel tex(latex) R-graphics R-prodlim R-stats 

%description
Estimation of the bivariate distribution function for sequentially ordered
events under univariate censoring

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
%doc %{rlibdir}/survivalBIV/DESCRIPTION
%doc %{rlibdir}/survivalBIV/html
%{rlibdir}/survivalBIV/NAMESPACE
%{rlibdir}/survivalBIV/libs
%{rlibdir}/survivalBIV/R
%{rlibdir}/survivalBIV/data
%{rlibdir}/survivalBIV/Meta
%{rlibdir}/survivalBIV/help
%{rlibdir}/survivalBIV/INDEX
%{rlibdir}/survivalBIV/NEWS.Rd

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora