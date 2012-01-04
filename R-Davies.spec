%global packname  Davies
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          The Davies quantile function

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Various utilities for the Davies distribution and the generalized lambda

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
%doc %{rlibdir}/Davies/html
%doc %{rlibdir}/Davies/DESCRIPTION
%doc %{rlibdir}/Davies/CITATION
%{rlibdir}/Davies/Meta
%{rlibdir}/Davies/data
%{rlibdir}/Davies/NAMESPACE
%{rlibdir}/Davies/R
%{rlibdir}/Davies/INDEX
%{rlibdir}/Davies/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.7-1
- initial package for Fedora