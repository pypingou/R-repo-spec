%global packname  tspair
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Top Scoring Pairs for Microarray Classification

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-time 

BuildRequires:    R-devel tex(latex) R-Biobase R-time 

%description
These functions calculate the pair of genes that show the maximum
difference in ranking between two user specified groups. This "top scoring
pair" maximizes the average of sensitivity and specificity over all  rank
based classifiers using a pair of genes in the data set. The advantage of
classifying samples based on only the relative rank of a pair of genes is
(a) the classifiers are much simpler and often more interpretable than
more complicated classification schemes and (b) if arrays can be
classified using only a pair of genes, PCR based tests could be used for
classification of samples. See the references for the tspcalc() function
for references regarding TSP classifiers.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora