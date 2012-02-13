%global packname  yaml
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.3
Release:          1%{dist}
Summary:          Methods to convert R to YAML and back

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package implements the libyaml YAML parser
(http://pyyaml.org/wiki/LibYAML) for R.  There are also methods to convert
R objects into YAML.

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
%doc %{rlibdir}/yaml/html
%doc %{rlibdir}/yaml/DESCRIPTION
%{rlibdir}/yaml/INDEX
%{rlibdir}/yaml/help
%{rlibdir}/yaml/CHANGELOG
%{rlibdir}/yaml/NAMESPACE
%{rlibdir}/yaml/implicit.re
%{rlibdir}/yaml/R
%{rlibdir}/yaml/THANKS
%{rlibdir}/yaml/Meta
%{rlibdir}/yaml/libs

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.3-1
- Update to version 2.1.3

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora