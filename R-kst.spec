%global packname  kst
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Knowledge Space Theory

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-proxy R-relations R-sets 


BuildRequires:    R-devel tex(latex) R-proxy R-relations R-sets



%description
Knowledge Space Theory is a set-theoretical framework, which proposes
mathematical formalisms to operationalize knowledge structures in a
particular domain. The kst-package provides basic functionalities to
generate, handle, and manipulate knowledge structures and knowledge

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
%doc %{rlibdir}/kst/doc
%doc %{rlibdir}/kst/html
%doc %{rlibdir}/kst/DESCRIPTION
%{rlibdir}/kst/help
%{rlibdir}/kst/INDEX
%{rlibdir}/kst/Meta
%{rlibdir}/kst/demo
RPM build errors:
%{rlibdir}/kst/R
%{rlibdir}/kst/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora