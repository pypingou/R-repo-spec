%global packname  homtest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Homogeneity tests for Regional Frequency Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
A collection of homogeneity tests described in: Viglione A., Laio F.,
Claps P. (2007) ``A comparison of homogeneity tests for regional frequency
analysis'', Water Resources Research, 43, W03428,
doi:10.1029/2006WR005095. More on Regional Frequency Analysis can be found
in package nsRFA.

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
%doc %{rlibdir}/homtest/html
%doc %{rlibdir}/homtest/DESCRIPTION
%{rlibdir}/homtest/data
%{rlibdir}/homtest/NAMESPACE
%{rlibdir}/homtest/INDEX
%{rlibdir}/homtest/R
%{rlibdir}/homtest/Meta
%{rlibdir}/homtest/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora