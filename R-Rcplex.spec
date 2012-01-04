%global packname  Rcplex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          R interface to CPLEX

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-slam 


BuildRequires:    R-devel tex(latex) R-slam



%description
R interface to CPLEX solvers for linear, quadratic, and (linear and
quadratic) mixed integer programs. Support for quadratically constrained
programming is available. A working installation of CPLEX is required for
usage of the Rcplex package. See the file "INSTALL" for details on how to
install the Rcplex package in Linux/Unix-like systems and Windows systems.
Support for sparse matrices is provided by an S3-style class
"simple_triplet_matrix" from package slam and by objects from the Matrix
package class hierarchy.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora