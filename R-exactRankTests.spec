%global packname  exactRankTests
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.22
Release:          1%{?dist}
Summary:          Exact Distributions for Rank and Permutation Tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-22.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-utils R-survival 

BuildRequires:    R-devel tex(latex) R-stats R-utils R-survival 

%description
Computes exact conditional p-values and quantiles using an implementation
of the Shift-Algorithm by Streitberg & Roehmel.

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
%doc %{rlibdir}/exactRankTests/html
%doc %{rlibdir}/exactRankTests/DESCRIPTION
%{rlibdir}/exactRankTests/Meta
%{rlibdir}/exactRankTests/libs
RPM build errors:
%{rlibdir}/exactRankTests/data
%{rlibdir}/exactRankTests/NAMESPACE
%{rlibdir}/exactRankTests/R
%{rlibdir}/exactRankTests/INDEX
%{rlibdir}/exactRankTests/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.22-1
- initial package for Fedora