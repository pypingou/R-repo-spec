%global packname  corrperm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Permutation Tests of Correlation with Repeated Measurements

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Three permutation tests of correlation useful when there are repeated

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
%doc %{rlibdir}/corrperm/html
%doc %{rlibdir}/corrperm/DESCRIPTION
%{rlibdir}/corrperm/Meta
%{rlibdir}/corrperm/INDEX
%{rlibdir}/corrperm/R
%{rlibdir}/corrperm/NAMESPACE
%{rlibdir}/corrperm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora