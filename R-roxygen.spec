%global packname  roxygen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Literate Programming in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-digest 

BuildRequires:    R-devel tex(latex) R-digest 

%description
A Doxygen-like in-source documentation system for Rd, collation, namespace
and callgraphs.

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
%doc %{rlibdir}/roxygen/doc
%doc %{rlibdir}/roxygen/html
%doc %{rlibdir}/roxygen/DESCRIPTION
%{rlibdir}/roxygen/help
%{rlibdir}/roxygen/INDEX
%{rlibdir}/roxygen/Meta
%{rlibdir}/roxygen/libs
%{rlibdir}/roxygen/R
%{rlibdir}/roxygen/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora