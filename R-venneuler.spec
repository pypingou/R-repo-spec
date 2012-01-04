%global packname  venneuler
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Venn and Euler Diagrams

Group:            Applications/Engineering 
License:          MPL-1.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Calculates and displays Venn and Euler Diagrams

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
%doc %{rlibdir}/venneuler/html
%doc %{rlibdir}/venneuler/NEWS
%doc %{rlibdir}/venneuler/DESCRIPTION
%{rlibdir}/venneuler/NAMESPACE
%{rlibdir}/venneuler/R
%{rlibdir}/venneuler/java
%{rlibdir}/venneuler/INDEX
%{rlibdir}/venneuler/Meta
%{rlibdir}/venneuler/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora