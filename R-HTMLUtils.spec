%global packname  HTMLUtils
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Facilitates automated HTML report creation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R2HTML 

BuildRequires:    R-devel tex(latex) R-R2HTML 

%description
Facilitates automated HTML report creation, in particular framed HTML
pages and dynamically sortable tables.

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
%doc %{rlibdir}/HTMLUtils/html
%doc %{rlibdir}/HTMLUtils/DESCRIPTION
%{rlibdir}/HTMLUtils/jsc
%{rlibdir}/HTMLUtils/R
%{rlibdir}/HTMLUtils/help
%{rlibdir}/HTMLUtils/Meta
%{rlibdir}/HTMLUtils/NAMESPACE
%{rlibdir}/HTMLUtils/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora