%global packname  magma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2.1
Release:          1%{?dist}
Summary:          Matrix Algebra on GPU and Multicore Architectures

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Magma matrix classes and methods for parallel processing of matrix algebra
operations.  Operations are performed with algorithms developed by the
MAGMA research project.  MAGMA aims to achieve the fastest possible linear
algebra libraries on hybrid multicore CPU and GPU architectures by
exploiting their massive parallelism and minimizing communication

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2.1-1
- initial package for Fedora