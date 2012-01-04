%global packname  neldermead
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          R port of the Scilab neldermead module

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-optimbase R-optimsimplex 

BuildRequires:    R-devel tex(latex) R-optimbase R-optimsimplex 

%description
Provides several direct search optimization algorithms based on the
simplex method. The provided algorithms are direct search algorithms, i.e.
algorithms which do not use the derivative of the cost function. They are
based on the update of a simplex. The following algorithms are available:
the fixed shape simplex method of Spendley, Hext and Himsworth
(unconstrained optimization with a fixed shape simplex), the variable
shape simplex method of Nelder and Mead (unconstrained optimization with a
variable shape simplex made), and Box's complex method (constrained
optimization with a variable shape simplex).

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
%doc %{rlibdir}/neldermead/html
%doc %{rlibdir}/neldermead/DESCRIPTION
%doc %{rlibdir}/neldermead/doc
%{rlibdir}/neldermead/INDEX
%{rlibdir}/neldermead/Meta
%{rlibdir}/neldermead/NAMESPACE
%{rlibdir}/neldermead/help
%{rlibdir}/neldermead/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora