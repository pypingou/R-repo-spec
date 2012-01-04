%global packname  PoissonSeq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Significance analysis of sequencing data based on a Poisson log linear model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-combinat R-splines 

BuildRequires:    R-devel tex(latex) R-combinat R-splines 

%description
This package implements a method for normalization, testing, and false
discovery rate estimation for RNA-sequencing data. The description of the
method is in Li J, Witten DM, Johnstone I, Tibshirani R (2011).
Normalization, testing, and false discovery rate estimation for
RNA-sequencing data. To appear, Biostatistics. We estimate the sequencing
depths of experiments using a new method based on Poisson goodness-of-fit
statistic, calculate a score statistic on the basis of a Poisson
log-linear model, and then estimate the false discovery rate using a
modified version of permutation plug-in method. A more detailed
instruction as well as sample data is available at

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
%doc %{rlibdir}/PoissonSeq/DESCRIPTION
%doc %{rlibdir}/PoissonSeq/html
%{rlibdir}/PoissonSeq/INDEX
%{rlibdir}/PoissonSeq/help
%{rlibdir}/PoissonSeq/LICENSE
%{rlibdir}/PoissonSeq/data
%{rlibdir}/PoissonSeq/NAMESPACE
%{rlibdir}/PoissonSeq/R
%{rlibdir}/PoissonSeq/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora