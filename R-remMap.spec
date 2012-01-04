%global packname  remMap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Regularized Multivariate Regression for Identifying Master Predictors

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
remMap is developed for fitting multivariate response regression models
under the high-dimension-low-sample-size setting

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
%doc %{rlibdir}/remMap/html
%doc %{rlibdir}/remMap/DESCRIPTION
%{rlibdir}/remMap/NAMESPACE
%{rlibdir}/remMap/Meta
%{rlibdir}/remMap/help
%{rlibdir}/remMap/INDEX
%{rlibdir}/remMap/R
%{rlibdir}/remMap/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora