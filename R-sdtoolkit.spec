%global packname  sdtoolkit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.31
Release:          1%{?dist}
Summary:          Scenario Discovery Tools to Support Robust Decision Making

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implements algorithms to help with scenario discovery - currently only
modified version of the the Patient Rule Induction Method.

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
%doc %{rlibdir}/sdtoolkit/DESCRIPTION
%doc %{rlibdir}/sdtoolkit/html
%{rlibdir}/sdtoolkit/R
%{rlibdir}/sdtoolkit/help
%{rlibdir}/sdtoolkit/NAMESPACE
%{rlibdir}/sdtoolkit/INDEX
%{rlibdir}/sdtoolkit/Meta
%{rlibdir}/sdtoolkit/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.31-1
- initial package for Fedora