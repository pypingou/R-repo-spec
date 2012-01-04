%global packname  denpro
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Visualization of multivariate, functions, sets, and data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package provides tools to (1) visualize multivariate density functions
and density estimates with level set trees, (2) visualize level sets with
shape trees, (3) visualize multivariate data with tail trees, (4)
visualize scales of multivariate density estimates with mode graphs and
branching maps, and (5) visualize anisotropic spread with 2D volume
functions and 2D probability conetent functions. Level set trees visualize
mode structure, shape trees visualize shapes of level sets of unimodal
densities, and tail trees visualize connected data sets. The kernel
estimator is implemented but the package may be applied for visualizing
other density estimates.

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
%doc %{rlibdir}/denpro/html
%doc %{rlibdir}/denpro/DESCRIPTION
%{rlibdir}/denpro/Meta
%{rlibdir}/denpro/libs
%{rlibdir}/denpro/NAMESPACE
%{rlibdir}/denpro/R
%{rlibdir}/denpro/INDEX
%{rlibdir}/denpro/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora