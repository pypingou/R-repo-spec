%global packname  spatialkernel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.10
Release:          1%{?dist}
Summary:          Nonparameteric estimation of spatial segregation in a multivariate point process

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Edge-corrected kernel density estimation and binary kernel regression
estimation for multivariate spatial point process data

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
%doc %{rlibdir}/spatialkernel/html
%doc %{rlibdir}/spatialkernel/DESCRIPTION
%{rlibdir}/spatialkernel/help
%{rlibdir}/spatialkernel/NAMESPACE
%{rlibdir}/spatialkernel/libs
%{rlibdir}/spatialkernel/R
%{rlibdir}/spatialkernel/data
%{rlibdir}/spatialkernel/INDEX
%{rlibdir}/spatialkernel/LICENSE
%{rlibdir}/spatialkernel/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.10-1
- initial package for Fedora