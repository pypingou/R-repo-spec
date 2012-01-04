%global packname  wikibooks
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions and datasets of the german WikiBook "GNU R"

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The german Wikibook "GNU R" introduces R to new users. This package is a
collection of functions and datas used in the german WikiBook "GNU R"

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
%doc %{rlibdir}/wikibooks/html
%doc %{rlibdir}/wikibooks/DESCRIPTION
%{rlibdir}/wikibooks/INDEX
%{rlibdir}/wikibooks/data
%{rlibdir}/wikibooks/Meta
%{rlibdir}/wikibooks/NAMESPACE
%{rlibdir}/wikibooks/R
%{rlibdir}/wikibooks/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora