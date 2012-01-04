%global packname  vegan
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Community Ecology Package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-permute 
Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-permute
BuildRequires:    R-lattice 


%description
Ordination methods, diversity analysis and other functions for community
and vegetation ecologists.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora