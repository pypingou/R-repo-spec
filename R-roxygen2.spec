%global packname  roxygen2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          In-source documentation for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-digest 
Requires:         R-stringr R-tools R-brew 

BuildRequires:    R-devel tex(latex) R-digest
BuildRequires:    R-stringr R-tools R-brew 


%description
A Doxygen-like in-source documentation system for Rd, collation, and

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.2-1
- initial package for Fedora