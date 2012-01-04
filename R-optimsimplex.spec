%global packname  optimsimplex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          R port of the Scilab optimsimplex module

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-optimbase 

BuildRequires:    R-devel tex(latex) R-optimbase 

%description
Provides a building block for optimization algorithms based on a simplex.
The optimsimplex package may be used in the following optimization
methods: the simplex method of Spendley et al., the method of Nelder and
Mead, Box's algorithm for constrained optimization, the multi-dimensional
search by Torczon, etc...

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
%doc %{rlibdir}/optimsimplex/doc
%doc %{rlibdir}/optimsimplex/html
%doc %{rlibdir}/optimsimplex/DESCRIPTION
%{rlibdir}/optimsimplex/Meta
%{rlibdir}/optimsimplex/R
%{rlibdir}/optimsimplex/NAMESPACE
%{rlibdir}/optimsimplex/help
%{rlibdir}/optimsimplex/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora