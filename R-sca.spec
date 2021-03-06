%global packname  sca
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          Simple Component Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Simple Component Analysis often provides much more interpretable
components than Principal Components (PCA) without losing too much.

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
%doc %{rlibdir}/sca/DESCRIPTION
%doc %{rlibdir}/sca/html
%{rlibdir}/sca/help
%{rlibdir}/sca/R
%{rlibdir}/sca/docs
%{rlibdir}/sca/INDEX
%{rlibdir}/sca/NAMESPACE
%{rlibdir}/sca/data
%{rlibdir}/sca/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.7-1
- initial package for Fedora