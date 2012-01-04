%global packname  nnls
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          The Lawson-Hanson algorithm for non-negative least squares (NNLS)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R interface to the Lawson-Hanson implementation of an algorithm for
non-negative least squares (NNLS).  Also allows the combination of
non-negative and non-positive constraints.

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
%doc %{rlibdir}/nnls/html
%doc %{rlibdir}/nnls/DESCRIPTION
%{rlibdir}/nnls/R
%{rlibdir}/nnls/libs
%{rlibdir}/nnls/NAMESPACE
%{rlibdir}/nnls/INDEX
%{rlibdir}/nnls/Meta
%{rlibdir}/nnls/COPYRIGHTS
%{rlibdir}/nnls/help
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora