%global packname  LLAhclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Hierarchical clustering of variables or objects based on the likelihood linkage analysis method

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The likelihood linkage analysis is a general agglomerative hierarchical
clustering method developed in France by Lerman in a long series of
research articles and books. Initially proposed in the framework of
variable clustering, it has been progressively extended to allow the
clustering of very general object descriptions. The approach mainly
consists in replacing the value of the estimated similarity coefficient by
the probability of finding a lower value under the hypothesis of 'absence
of link'. The package LLAhclust contains routines for computing various
types of probablistic similarity coefficients between variables or object
descriptions. Once the similarity values between variables/objects are
computed, a hierarchical clustering can be performed using several
probabilistic and non-probabilistic aggregation criteria, and indices
measuring the quality of the partitions compatible with the resulting
hierarchy can be computed.

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
%doc %{rlibdir}/LLAhclust/html
%doc %{rlibdir}/LLAhclust/DESCRIPTION
%{rlibdir}/LLAhclust/libs
%{rlibdir}/LLAhclust/R
%{rlibdir}/LLAhclust/help
%{rlibdir}/LLAhclust/Meta
%{rlibdir}/LLAhclust/NAMESPACE
%{rlibdir}/LLAhclust/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora