%global packname  FD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Measuring functional diversity (FD) from multiple traits, and other tools for functional ecology

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ade4 R-ape R-geometry R-vegan 


BuildRequires:    R-devel tex(latex) R-ade4 R-ape R-geometry R-vegan



%description
FD is a package to compute different multidimensional FD indices. It
implements a distance-based framework to measure FD that allows any number
and type of functional traits, and can also consider species relative
abundances. It also contains other useful tools for functional ecology.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.11-1
- initial package for Fedora