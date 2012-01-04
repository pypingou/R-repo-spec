%global packname  openNLPmodels.en
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          openNLP Models for English

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
openNLP models for the English language.

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
%doc %{rlibdir}/openNLPmodels.en/html
%doc %{rlibdir}/openNLPmodels.en/DESCRIPTION
%{rlibdir}/openNLPmodels.en/Meta
%{rlibdir}/openNLPmodels.en/NAMESPACE
%{rlibdir}/openNLPmodels.en/models
%{rlibdir}/openNLPmodels.en/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4-1
- initial package for Fedora