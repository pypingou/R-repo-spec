%global packname  TERAplusB
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Test for A+B Traditional Escalation Rule

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is for the comparison of various types of A+B escalation
rules for dose finding trials.

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
%doc %{rlibdir}/TERAplusB/DESCRIPTION
%doc %{rlibdir}/TERAplusB/html
%{rlibdir}/TERAplusB/R
%{rlibdir}/TERAplusB/Meta
%{rlibdir}/TERAplusB/INDEX
%{rlibdir}/TERAplusB/NAMESPACE
%{rlibdir}/TERAplusB/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora