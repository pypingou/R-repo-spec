%global packname  MAd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Meta-Analysis with Mean Differences

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is an integrated meta-analysis package for conducting a research
synthesis with mean differences data. One of the unique features of this
package is in its integration of user-friendly functions to facilitate
statistical analyses at each stage in a meta-analysis with mean
differences. It uses recommended procedures as described in The Handbook
of Research Synthesis and Meta-Analysis (Cooper, Hedges, & Valentine,

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
%doc %{rlibdir}/MAd/doc
%doc %{rlibdir}/MAd/html
%doc %{rlibdir}/MAd/DESCRIPTION
%{rlibdir}/MAd/Meta
%{rlibdir}/MAd/INDEX
%{rlibdir}/MAd/R
%{rlibdir}/MAd/NAMESPACE
%{rlibdir}/MAd/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora