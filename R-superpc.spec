%global packname  superpc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.08
Release:          1%{?dist}
Summary:          Supervised principal components

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Supervised principal components for regression and survival analsysis.
Especially useful for high-dimnesional data, including microarray data.

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
%doc %{rlibdir}/superpc/html
%doc %{rlibdir}/superpc/DESCRIPTION
%{rlibdir}/superpc/Meta
%{rlibdir}/superpc/INDEX
%{rlibdir}/superpc/R
%{rlibdir}/superpc/NAMESPACE
%{rlibdir}/superpc/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.08-1
- initial package for Fedora