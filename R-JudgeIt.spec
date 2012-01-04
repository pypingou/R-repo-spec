%global packname  JudgeIt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          JudgeIt

Group:            Applications/Engineering 
License:          GPL version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Calculates bias, responsiveness, and other characteristics of two-party
electoral systems, with district-level electoral and other data.

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
%doc %{rlibdir}/JudgeIt/doc
%doc %{rlibdir}/JudgeIt/html
%doc %{rlibdir}/JudgeIt/DESCRIPTION
%{rlibdir}/JudgeIt/Meta
%{rlibdir}/JudgeIt/R
%{rlibdir}/JudgeIt/data
%{rlibdir}/JudgeIt/help
%{rlibdir}/JudgeIt/demo
%{rlibdir}/JudgeIt/NAMESPACE
%{rlibdir}/JudgeIt/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.3-1
- initial package for Fedora