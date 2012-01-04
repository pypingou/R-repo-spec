%global packname  MultEq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Multiple Equivalence Tests and Simultaneous Confidence Intervals

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Equivalence tests and related confidence intervals for the comparison of
two treatments, simultaneously for one or many normally distributed,
primary response variables (endpoints). The step-up procedure of Quan et
al. (2001) is both applied for differences and extended to ratios of
means. A related single-step procedure is also available.

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
%doc %{rlibdir}/MultEq/DESCRIPTION
%doc %{rlibdir}/MultEq/html
%{rlibdir}/MultEq/help
%{rlibdir}/MultEq/Meta
%{rlibdir}/MultEq/data
%{rlibdir}/MultEq/NAMESPACE
%{rlibdir}/MultEq/INDEX
%{rlibdir}/MultEq/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora