%global packname  simco
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          A package to import Structure files and deduce similarity coefficients from them

Group:            Applications/Engineering 
License:          GNU General Public License
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) R-gtools 

%description
Simco is a package that (1) imports Structure output files into R and (2)
carries out similarity coefficient calculations on them.

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
%doc %{rlibdir}/simco/LICENCE
%doc %{rlibdir}/simco/html
%doc %{rlibdir}/simco/DESCRIPTION
%{rlibdir}/simco/R
%{rlibdir}/simco/NAMESPACE
%{rlibdir}/simco/Meta
%{rlibdir}/simco/help
%{rlibdir}/simco/data
%{rlibdir}/simco/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora