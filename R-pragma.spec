%global packname  pragma
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Provides a pragma / directive / keyword syntax for R.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-utils R-methods 

%description
pragma allows for the use of pragma (also sometimes called directives or
keywords. These allow assigning arbitrary functionality to a word without
requiring the standard function call syntax i.e. with parens.

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
%doc %{rlibdir}/pragma/DESCRIPTION
%doc %{rlibdir}/pragma/html
%doc %{rlibdir}/pragma/NEWS
%{rlibdir}/pragma/help
%{rlibdir}/pragma/Meta
%{rlibdir}/pragma/NAMESPACE
%{rlibdir}/pragma/INDEX
%{rlibdir}/pragma/R
%{rlibdir}/pragma/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora