%global packname  RobustRankAggreg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Methods for robust rank aggregation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Methods for aggregating ranked lists, especially lists of genes. It
implements the Robust Rank Aggregation (Kolde et. al in preparation) and
some other simple algorithms for the task. RRA method uses a probabilistic
model for aggregation that is robust to noise and also facilitates the
calculation of significance probabilities for all the elements in the
final ranking.

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
%doc %{rlibdir}/RobustRankAggreg/html
%doc %{rlibdir}/RobustRankAggreg/DESCRIPTION
%{rlibdir}/RobustRankAggreg/R
%{rlibdir}/RobustRankAggreg/help
%{rlibdir}/RobustRankAggreg/INDEX
%{rlibdir}/RobustRankAggreg/NAMESPACE
%{rlibdir}/RobustRankAggreg/Meta
%{rlibdir}/RobustRankAggreg/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora