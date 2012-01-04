%global packname  MergeMaid
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.26.0
Release:          1%{?dist}
Summary:          Merge Maid

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-Biobase R-MASS R-methods 

BuildRequires:    R-devel tex(latex) R-survival R-Biobase R-MASS R-methods 

%description
The functions in this R extension are intended for cross-study comparison
of gene expression array data. Required from the user is gene expression
matrices, their corresponding gene-id vectors and other useful
information, and they could be 'list','matrix', or 'ExpressionSet'. The
main function is 'mergeExprs' which transforms the input objects into data
in the merged format, such that common genes in different datasets can be
easily found. And the function 'intcor' calculate the correlation
coefficients. Other functions use the output from 'modelOutcome' to
graphically display the results and cross-validate associations of gene
expression data with survival.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.26.0-1
- initial package for Fedora