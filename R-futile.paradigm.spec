%global packname  futile.paradigm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          A framework for working in a functional programming paradigm in R

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-futile.options 

BuildRequires:    R-devel tex(latex) R-futile.options 

%description
Provides dispatching implementations suitable for functional programming
paradigms. The framework provides a mechanism for attaching guards to
functions similar to Erlang, while also providing the safety of assertions
reminiscent of Eiffel.

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
%doc %{rlibdir}/futile.paradigm/html
%doc %{rlibdir}/futile.paradigm/DESCRIPTION
%{rlibdir}/futile.paradigm/unitTests
%{rlibdir}/futile.paradigm/help
%{rlibdir}/futile.paradigm/R
%{rlibdir}/futile.paradigm/NAMESPACE
%{rlibdir}/futile.paradigm/Meta
%{rlibdir}/futile.paradigm/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora