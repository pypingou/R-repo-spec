%global packname  AtelieR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.22
Release:          1%{?dist}
Summary:          A GTK GUI for teaching basic concepts in statistical inference, and doing elementary bayesian tests.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-proto R-cairoDevice R-gWidgetsRGtk2 R-partitions 


BuildRequires:    R-devel tex(latex) R-proto R-cairoDevice R-gWidgetsRGtk2 R-partitions



%description
A collection of statistical simulation and computation tools with a GTK
GUI, to help teach statistical concepts and compute probabilities. Two
domains are covered: I. Understanding (Central-Limit Theorem and the
Normal Distribution, Distribution of a sample mean, Distribution of a
sample variance, Probability calculator for common distributions), and II.
Elementary Bayesian Statistics (bayesian inference on proportions,
contingency tables, means and variances, with informative and
noninformative priors).

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.22-1
- initial package for Fedora