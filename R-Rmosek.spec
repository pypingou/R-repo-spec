%global packname  Rmosek
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          The R-to-MOSEK Optimization Interface

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Rmosek is an interface to the MOSEK Optimization Software designed to
solve large-scale mathematical optimization problems. MOSEK provides
specialized solvers for linear programming, mixed integer programming and
many types of nonlinear convex optimization problems. Trial and free
academic licenses available at http://www.mosek.com.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.5-1
- initial package for Fedora