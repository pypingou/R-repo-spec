%global packname  ssanv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Sample Size Adjusted for Nonadherence or Variability of input parameters

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
A set of functions to calculate sample size for two-sample difference in
means tests. Does adjustments for either nonadherence or variability that
comes from using data to estimate parameters.

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
%doc %{rlibdir}/ssanv/CITATION
%doc %{rlibdir}/ssanv/html
%doc %{rlibdir}/ssanv/DESCRIPTION
%{rlibdir}/ssanv/help
%{rlibdir}/ssanv/R
%{rlibdir}/ssanv/INDEX
%{rlibdir}/ssanv/NAMESPACE
%{rlibdir}/ssanv/data
%{rlibdir}/ssanv/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora