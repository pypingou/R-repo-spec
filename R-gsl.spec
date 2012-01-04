%global packname  gsl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.9
Release:          1%{?dist}
Summary:          wrapper for the Gnu Scientific Library

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R wrapper for the special functions and quasi random number generators
of the Gnu Scientific Library (http://www.gnu.org/software/gsl/).  See
gsl-package.Rd for details of overall package organization, and Misc.Rd
for some functions that are widely used in the package, and some tips on

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.9-1
- initial package for Fedora