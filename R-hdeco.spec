%global packname  hdeco
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Hierarchical DECOmposition of Entropy for Categorical Map Comparisons

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A flexible and hierarchical framework for comparing categorical map
composition and configuration (spatial pattern) along spatial, thematic,
or external grouping variables.  Comparisons are based on measures of
mutual information between thematic classes (colours) and location
(spatial partitioning).  Results are returned in textual, tabular, and
graphical forms.

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
%doc %{rlibdir}/hdeco/DESCRIPTION
%doc %{rlibdir}/hdeco/html
%{rlibdir}/hdeco/help
%{rlibdir}/hdeco/data
%{rlibdir}/hdeco/Meta
%{rlibdir}/hdeco/R
%{rlibdir}/hdeco/INDEX
%{rlibdir}/hdeco/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora