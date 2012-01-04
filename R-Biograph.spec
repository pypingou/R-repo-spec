%global packname  Biograph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Explore life histories

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Epi R-msm R-mvna R-survival 


BuildRequires:    R-devel tex(latex) R-Epi R-msm R-mvna R-survival



%description
Extracts from the data useful information on the life courses of selected
individuals or subpopulations with given attributes.

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
%doc %{rlibdir}/Biograph/DESCRIPTION
%doc %{rlibdir}/Biograph/html
%{rlibdir}/Biograph/data
%{rlibdir}/Biograph/R
%{rlibdir}/Biograph/help
%{rlibdir}/Biograph/INDEX
%{rlibdir}/Biograph/Meta
%{rlibdir}/Biograph/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora