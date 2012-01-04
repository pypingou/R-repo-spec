%global packname  twilight
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          Estimation of local false discovery rate

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-stats R-Biobase 

BuildRequires:    R-devel tex(latex) R-splines R-stats R-Biobase 

%description
In a typical microarray setting with gene expression data observed under
two conditions, the local false discovery rate describes the probability
that a gene is not differentially expressed between the two conditions
given its corrresponding observed score or p-value level. The resulting
curve of p-values versus local false discovery rate offers an insight into
the twilight zone between clear differential and clear non-differential
gene expression. Package 'twilight' contains two main functions: Function
twilight.pval performs a two-condition test on differences in means for a
given input matrix or expression set and computes permutation based
p-values. Function twilight performs a stochastic downhill search to
estimate local false discovery rates and effect size distributions. The
package further provides means to filter for permutations that describe
the null distribution correctly. Using filtered permutations, the
influence of hidden confounders could be diminished.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora