%global packname  rrdflibs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          rrdflibs - package with Jena and Apache HTTP libraries for use with rrdf

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Jena RDF and Apache HTTP Client libraries. Jena and HTTPClient are
distributed under their original licenses.

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
%doc %{rlibdir}/rrdflibs/DESCRIPTION
%doc %{rlibdir}/rrdflibs/html
%{rlibdir}/rrdflibs/help
%{rlibdir}/rrdflibs/java
%{rlibdir}/rrdflibs/Meta
%{rlibdir}/rrdflibs/R
%{rlibdir}/rrdflibs/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora