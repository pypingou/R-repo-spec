%global packname  SimComp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Simultaneous Comparisons for Multiple Endpoints

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-mvtnorm R-multcomp R-mratios 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-mvtnorm R-multcomp R-mratios 


%description
Simultaneous tests and confidence intervals for one-way experimental
designs with one or many normally distributed, primary response variables
(endpoints). The procedure of Hasler and Hothorn (2011) is applied for
differences or ratios of means. Various contrasts can be chosen,
unbalanced sample sizes are allowed as well as heterogeneous variances or
covariance matrices.

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
%doc %{rlibdir}/SimComp/DESCRIPTION
%doc %{rlibdir}/SimComp/html
%{rlibdir}/SimComp/INDEX
%{rlibdir}/SimComp/R
%{rlibdir}/SimComp/data
%{rlibdir}/SimComp/NAMESPACE
%{rlibdir}/SimComp/Meta
%{rlibdir}/SimComp/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora