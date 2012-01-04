%global packname  RScaLAPACK
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          A seamless interface to perform parallel computation on linear algebra problems using the ScaLAPACK library.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R add-on package capable of carrying out parallel computation through a
single function call from the R environment. It uses the high-performance
ScaLAPACK library for the linear algebra computations.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora