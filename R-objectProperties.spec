%global packname  objectProperties
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{dist}
Summary:          A factory of self-describing properties.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-objectSignals 

BuildRequires:    R-devel tex(latex) R-methods R-objectSignals 

%description
Supports the definition of sets of properties on objects. Observers can
listen to changes on individual properties or the set as a whole. The
properties are meant to be fully self-describing. In support of this,
there is a framework for defining enumerated types, as well as other
bounded types, as S4 classes.

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
%doc %{rlibdir}/objectProperties/html
%doc %{rlibdir}/objectProperties/DESCRIPTION
%doc %{rlibdir}/objectProperties/NEWS
%{rlibdir}/objectProperties/help
%{rlibdir}/objectProperties/INDEX
%{rlibdir}/objectProperties/examples
%{rlibdir}/objectProperties/Meta
%{rlibdir}/objectProperties/R
%{rlibdir}/objectProperties/NAMESPACE

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- Update to version 0.6.5

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora