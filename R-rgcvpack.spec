%global packname  rgcvpack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          R Interface for GCVPACK Fortran Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Thin plate spline fitting and prediction

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
%doc %{rlibdir}/rgcvpack/doc
%doc %{rlibdir}/rgcvpack/html
%doc %{rlibdir}/rgcvpack/DESCRIPTION
%{rlibdir}/rgcvpack/INDEX
%{rlibdir}/rgcvpack/R
%{rlibdir}/rgcvpack/NAMESPACE
%{rlibdir}/rgcvpack/libs
%{rlibdir}/rgcvpack/Meta
%{rlibdir}/rgcvpack/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora