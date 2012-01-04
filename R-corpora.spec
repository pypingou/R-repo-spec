%global packname  corpora
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.2.1
Release:          1%{?dist}
Summary:          Statistics for corpus linguists

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-2.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Utility functions for the statistical analysis of corpus frequency data

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
%doc %{rlibdir}/corpora/html
%doc %{rlibdir}/corpora/DESCRIPTION
%{rlibdir}/corpora/INDEX
%{rlibdir}/corpora/R
%{rlibdir}/corpora/data
%{rlibdir}/corpora/NAMESPACE
%{rlibdir}/corpora/Meta
%{rlibdir}/corpora/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.2.1-1
- initial package for Fedora